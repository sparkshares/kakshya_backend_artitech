from openai import OpenAI
import os
import json
from assignments.models.assignment_transaction import AssignmentTransaction

from assignments.serializers.assignment_grading_serializer import AssignmentGradingSerializer
from assignments.serializers.assignment_transaction_serializer import AssignmentTransactionSerializer

api_key = os.getenv('OPENAI_API_KEY')

def gpt_grade_assignment(assignment_text, transaction_text, grade_detail, remark, transaction_id, transaction_text2):
    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
               {"role": "system", "content": "Imagine you are a teacher Follow the pattern like teacher and Please grade and give me the logical answer response in json format like this {'grade':'HERE YOUR GIVEN GRADE','remark':'HERE YOUR GIVEN REMARK'}."},
               {"role": "user", "content": f"The Assignment given by teacher is this : {assignment_text}\n Example Student Response is this : {transaction_text} , Grade given by teacher was this : {grade_detail} and Remark give by teacher was : {remark} , now image you are a teacher, now for this assignment, now please give a valid grade for this assignment and a detailed remark submitted by student, his assignment text was this {transaction_text2}, now give me the json response of grade and remark"},
        ]
    )

    # Get the content from the response
    content = response.choices[0].message.content
    
    print(content)

    # Remove the markdown code block identifiers
    content = content.replace("```json\n", "").replace("\n```", "")

    # Convert the string to a JSON object
    json_response = json.loads(content)

    # Save the response to the AssignmentGrading table
    grading_data = {
        'as_trans_id': transaction_id,
        'grade': json_response['grade'],
        'remark': json_response['remark']
    }
    grading_serializer = AssignmentGradingSerializer(data=grading_data)
    if grading_serializer.is_valid():
        grading_serializer.save()


    return {"Status":"Success for "+str(transaction_id)}
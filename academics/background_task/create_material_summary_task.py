# tasks.py
from academics.models.subject_material import SubjectMaterial
from academics.serializers.subject_material_text_serializer import SubjectMaterialTextSerializer
from celery import shared_task
from openai import OpenAI
import os

from testing.test import extract_text_from_file

# Ensure your OPENAI_API_KEY is set in your environment variables
api_key = os.getenv('OPENAI_API_KEY')

@shared_task
def create_material_summary_task(sub_mat_id, file_path):
    try:
        # Initialize OpenAI client
        client = OpenAI(api_key=api_key)

        # Process and summarize the file content
        initial_summary = extract_text_from_file(file_path)

        # Send the initial summary to GPT-3.5-turbo for further summarization
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role": "system", "content": "Summarize the topics I will ask you questions in future from this context so summarize it so you can remember everything so when I ask you anything next time you remember everything. no don't say sure or anything, just give me full summary, make sure to include everything everytopic"},
                {"role": "user", "content": initial_summary}
            ]
        )

        # Extract the summarized content
        gpt_summary = response.choices[0].message.content

        # Save the final summary using the serializer
        subject_material = SubjectMaterial.objects.get(id=sub_mat_id)
        summary_data = {
            'material_text': gpt_summary,
            'sub_mat_id': subject_material.id,
            'status': 'Success'
        }
        summary_serializer = SubjectMaterialTextSerializer(data=summary_data)

        if summary_serializer.is_valid():
            summary_serializer.save()
            return {"message": "Material summary created successfully"}
        else:
            return {"message": "Serialization failed", "errors": summary_serializer.errors}
    except Exception as e:
        return {"message": f"Error in task execution: {str(e)}"}


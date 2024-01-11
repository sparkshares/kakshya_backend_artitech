from academics.models.class_record import ClassRecord
from academics.serializers.class_summary_serializer import ClassRecordSummarySerializer
from celery import shared_task
import json
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

api_key = os.getenv('OPENAI_API_KEY')

@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=True, max_retries=3)
def create_class_record_task(self, record_id, file_path):
    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)

    # Retrieve the ClassRecord from the record_id
    try:
        class_record = ClassRecord.objects.get(id=record_id)
    except ClassRecord.DoesNotExist:
        return {"message": "ClassRecord not found"}, 404

    try:
        # Process the audio file
        with open(file_path, 'rb') as audio:
            transcript = client.audio.translations.create(
                model="whisper-1", 
                file=audio
            )

        summarize = transcript.text

        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role": "system", "content": "Please give the summary of this in json format, 'summary' in json format is mandatory and summary value should be long"},
                {"role": "user", "content": summarize}
            ]
        )

        # Get the content from the response
        content = response.choices[0].message.content
        content = content.replace("```json\n", "").replace("\n```", "")
        json_response = json.loads(content)

        # Create a new ClassRecordSummary instance
        summary_data = {
            'summary': json_response['summary'],
            'record_id': class_record.id,
            'status': "Success"
        }
    except Exception as e:
        if self.request.retries == self.max_retries:
            summary_data = {
                'summary': "Unable to detect",
                'record_id': class_record.id,
                'status': "Failed"
            }
        else:
            raise self.retry(exc=e)

    summary_serializer = ClassRecordSummarySerializer(data=summary_data)
    if summary_serializer.is_valid():
        summary_serializer.save()
        return {"message": "Class summary created successfully"}, 200
    else:
        return summary_serializer.errors, 400
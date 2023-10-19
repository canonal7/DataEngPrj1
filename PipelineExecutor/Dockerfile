FROM python:3.10.7-slim
ADD PipelineExecutor.py /home/PipelineExecutor.py
ADD requirements.txt ./
RUN pip install -r requirements.txt
ENTRYPOINT ["python","/home/PipelineExecutor.py"]
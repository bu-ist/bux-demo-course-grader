from bux_grader_framework.evaluators import BaseEvaluator


class DummyEvaluator(BaseEvaluator):
    name = 'dummy'

    def evaluate(self, submission):
        body = submission['xqueue_body']
        grader_payload = body['grader_payload']

        student_answer = body['student_response']
        grader_answer = grader_payload['answer']

        if student_answer == grader_answer:
            return {"correct": True, "score": 1, "msg": "<p>Nice work!</p>"}
        else:
            return {"correct": False, "score": 0, "msg": "<p>Nice try!</p>"}

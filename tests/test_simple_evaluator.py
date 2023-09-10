from lm_eval import evaluator

# import lm_eval.models as models
import lm_eval.api as api
import lm_eval.evaluator as evaluator
import random
import pytest


# TODO: more fine grained unit tests rather than this big honking integration
# test once we break evaluator into smaller, more manageable pieces


@pytest.mark.parametrize(
    "task_name,model,model_args",
    [
        (
            # [
            # # 'drop'
            # # "multiple_choice"
            # "qnli"
            # ],
            ["can_you_infer_zs_promptsource"],
            # ["summarize_the_article_zs_promptsource"],
            "hf",
            "pretrained=HooshvareLab/gpt2-fa,dtype=float32,device=cuda",
        )
    ],
)
def test_evaluator(task_name: list[str], model: str, model_args: str):
    task_name = task_name
    limit=10
 
    e1 = evaluator.simple_evaluate(
        model=model,
        tasks=task_name,
        limit=limit,
        model_args=model_args,
    )
    assert e1 is not None

    def r(x):
        return x["results"]["arc_easy"]

    

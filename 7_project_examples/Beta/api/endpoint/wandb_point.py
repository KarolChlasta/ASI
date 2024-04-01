from api import APIRouter, FastAPI
import services.temporary_memory as memory
from services.cli import run_command as run_command
from startup import ENV_NAME

router = APIRouter()


@router.post("/login_wandb/")
def login_wandb(api_key: str):
    _, _, err = run_command(f"conda activate {ENV_NAME} & wandb login " + api_key, )
    if err:
        return {"message": "Invalid API key"}
    memory.wandb_key = api_key
    return {"message": "Success"}

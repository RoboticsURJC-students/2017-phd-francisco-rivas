
import torchvision
from models.backends.custom.pilotnet import PilotNet
from torchvision.models.resnet import resnet18

AVAILABLE_BACKENDS=[
    "mobilenet_v3_small",
    "mobilenet_v3_large",
    "pilotnet"
]


def get_backend_by_name(backend_name):
    if backend_name not in AVAILABLE_BACKENDS:
        raise Exception("Backend name {} not available {}".format(backend_name, AVAILABLE_BACKENDS))

    if backend_name == "mobilenet_v3_large":
        return torchvision.models.mobilenet_v3_large
    elif backend_name == "mobilenet_v3_small":
        return torchvision.models.mobilenet_v3_small
    elif backend_name == "pilotnet":
        return PilotNet

    return None
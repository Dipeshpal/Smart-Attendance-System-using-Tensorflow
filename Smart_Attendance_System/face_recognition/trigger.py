from .Face_Recognition_with_TF.scripts.retrain import retrain_with_tf
from .Face_Recognition import start as st


def start():
    # Training with OPENCV
    st.start_training()

    print("Training Started with TF")
    # retrain with TF
    retrain_with_tf()


from face_recognition.Face_Recognition import start as st


def start(roll_no):
    enrollment_no, name, total_days, total_present_days, precentage = st.fetch_data(roll_no)
    return enrollment_no, name, total_days, total_present_days, precentage

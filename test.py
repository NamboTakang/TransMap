import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QDialog


class UserProfilePage(QWidget):
    def __init__(self, user_id):
        super(UserProfilePage, self).__init__()

        # Mock data, replace this with actual data retrieval logic
        self.user_data = self.get_user_data(user_id)

        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        # Display user information
        self.user_info_label = QLabel(f"User Information for ID {self.user_data['user_id']}")
        self.layout.addWidget(self.user_info_label)

        # Display user details
        self.user_details_label = QLabel(
            f"Name: {self.user_data['name']}\nEmail: {self.user_data['email']}\nRole: {self.user_data['role']}")
        self.layout.addWidget(self.user_details_label)

        # Edit button
        edit_button = QPushButton("Edit Profile")
        edit_button.clicked.connect(self.edit_profile)
        self.layout.addWidget(edit_button)

        self.setLayout(self.layout)
        self.setWindowTitle("User Profile")

    def get_user_data(self, user_id):
        # Replace this with your actual data retrieval logic from the database
        return {
            'user_id': user_id,
            'name': 'Nambo Takang',
            'email': 'takang.nambo@ictuniversity.edu.cm',
            'role': 'User'
        }

    def edit_profile(self):
        edit_profile_dialog = EditProfileDialog(self, self.user_data)
        result = edit_profile_dialog.exec_()  # Use exec_() to show the dialog as a modal

        # Update user details if changes were saved
        if result == QDialog.Accepted:
            self.user_data = edit_profile_dialog.get_edited_data()
            self.update_user_details()

    def update_user_details(self):
        # Update displayed user details
        self.user_details_label.setText(
            f"Name: {self.user_data['name']}\nEmail: {self.user_data['email']}\nRole: {self.user_data['role']}")


class EditProfileDialog(QDialog):
    def __init__(self, parent=None, user_data=None):
        super(EditProfileDialog, self).__init__(parent)
        self.user_data = user_data
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Add widgets for editing user profile
        self.name_label = QLabel("Name:")
        self.name_edit = QLineEdit(self.user_data['name'])

        self.email_label = QLabel("Email:")
        self.email_edit = QLineEdit(self.user_data['email'])

        self.role_label = QLabel("Role:")
        self.role_edit = QLineEdit(self.user_data['role'])

        layout.addWidget(self.name_label)
        layout.addWidget(self.name_edit)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_edit)
        layout.addWidget(self.role_label)
        layout.addWidget(self.role_edit)

        # Save button
        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_profile)
        layout.addWidget(save_button)

        self.setLayout(layout)
        self.setWindowTitle("Edit Profile")

    def save_profile(self):
        # Save edited user data
        self.user_data['name'] = self.name_edit.text()
        self.user_data['email'] = self.email_edit.text()
        self.user_data['role'] = self.role_edit.text()

        # Accept the dialog, indicating changes were saved
        self.accept()

    def get_edited_data(self):
        return self.user_data


if __name__ == '__main__':
    app = QApplication(sys.argv)
    user_id = 458878  # Replace with the actual user ID
    profile_page = UserProfilePage(user_id)
    profile_page.show()
    sys.exit(app.exec())
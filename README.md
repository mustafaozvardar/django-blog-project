# 📝 Django Blog Project

This is a blog application built with Django. It allows users to create, edit, and delete blog posts. The project also integrates with CKEditor for rich text editing and uses Crispy Forms for better form rendering.

## Features ✨

- 🖊️ Create, edit, and delete blog posts.
- 📝 Rich text editing with CKEditor.
- 🧹 Automatic file cleanup using `django-cleanup`.
- 📋 Form rendering with `django-crispy-forms` for improved UI.
- 📦 Easy deployment and management.

## Requirements 📦

To run this project, you'll need the following Python packages installed. They are listed in the `requirements.txt` file:

- Django==2.0
- django-ckeditor==5.4.0
- django-cleanup==2.1.0
- django-crispy-forms==1.7.2
- django-js-asset==1.0.0

## Installation 🚀

Follow these steps to get the Django Blog project up and running on your local machine.

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/django-blog.git
    cd django-blog
    ```

2. **Create a virtual environment:**

    It's recommended to use a virtual environment to manage dependencies.

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    Install the necessary Python packages from `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    Make sure your database is set up and migrate the existing models:

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**

    Create an admin user to manage the blog:

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    Start the Django development server:

    ```bash
    python manage.py runserver
    ```

    You can now access the blog at `http://127.0.0.1:8000/`.

## Usage 🎨

- Navigate to the admin panel at `http://127.0.0.1:8000/admin/` to manage blog posts.
- Create, edit, or delete posts directly from the admin interface.
- View the blog posts on the homepage.


## Troubleshooting 🛠️

- Ensure you are using the correct versions of Django and the associated packages.
- If you encounter any issues with CKEditor, ensure that the static files are correctly configured and collected.

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements 🙏

- [Django](https://www.djangoproject.com/) - The web framework used.
- [CKEditor](https://ckeditor.com/) - For providing a powerful rich text editor.
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - For beautiful form layouts.



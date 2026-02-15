from ..core import Docker

class DockerTemplates:
    @staticmethod
    def python_app(
        image: str = "python:3.11",
        workdir: str = "/app",
        requirements_file: str = "requirements.txt",
        copy_dir: str = "."
    ) -> Docker:
        d = Docker()
        d.FROM(image)
        d.WORKDIR(workdir)
        d.COPY(copy_dir, workdir)
        d.RUN(f"pip install -r {requirements_file}")
        d.CMD(["python", "main.py"], exec_form=True)
        return d

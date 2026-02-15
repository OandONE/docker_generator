from typing import Optional, Union

class Docker:
    def __init__(
        self,
        text: Optional[str] = None,
        _from: Optional[str] = None,
        run: Optional[str] = None,
        from_dir: Optional[str] = None,
        to_dir: Optional[str] = None,
        from_stage: Optional[str] = None,
        port: Optional[str] = None,
        cmd: Optional[str] = None,
        exec_form: bool = False,
        arg_key: Optional[str] = None,
        arg_value: Optional[str] = None,
        env_key: Optional[str] = None,
        env_value: Optional[str] = None,
    ):
        self.text_docker = ""
        if text:
            self.add_text(
                text=text
            )
        if _from:
            self.set_from(
                _from=_from
            )
        if run:
            self.run(
                command=run
            )
        if from_dir and to_dir:
            self.copy(
                from_dir=from_dir,
                to_dir=to_dir,
                from_stage=from_stage
            )
        if port:
            self.expose(
                port=port
            )
        if cmd:
            self.cmd(
                command=cmd,
                exec_form=exec_form
            )
        if arg_key and arg_value:
            self.arg(
                key=arg_key,
                value=arg_value
            )
        if env_key and env_value:
            self.env(
                key=env_key,
                value=env_value
            )

    def add_text(
        self,
        text: str
    ):
        self.text_docker += text + "\n"

    def set_from(
        self,
        _from: str,
        stage_name: Optional[str] = None
    ):
        line = f"FROM {_from}"
        if stage_name:
            line += f"AS {stage_name}"
        self.add_text(line)

    def run(
        self,
        command: str
    ):
        self.add_text(f"RUN {command}")

    def workdir(
        self,
        dir: str
    ):
        if not dir.startswith("/"):
            dir = f"/{dir}"
        self.add_text(f"WORKDIR {dir}")

    def copy(
        self,
        from_dir: str = ".",
        to_dir: str = ".",
        from_stage: Optional[str] = None
    ):
        line = f"COPY {from_dir} {to_dir}"
        if from_stage:
            line = f"COPY --from={from_stage} {from_dir} {to_dir}"
        self.add_text(line)

    def expose(
        self,
        port: str
    ):
        self.add_text(f"EXPOSE {port}")

    def cmd(
        self,
        command: Union[str,list[str]],
        exec_form: bool = False
    ):
        if exec_form and isinstance(command, list):
            formatted = "[" + ", ".join(f'"{c}"' for c in command) + "]"
            self.add_text(f'CMD {formatted}')
        else:
            if isinstance(command, list):
                command = " ".join(command)
            self.add_text(f'CMD {command}')
    
    def arg(
        self,
        key: str,
        value: str
    ):
        self.add_text(f"ARG {key}={value}")

    def env(
        self,
        key: str,
        value: str
    ):
        self.add_text(f"ENV {key}={value}")

    def helpthcheck(
        self
    ):
        self.add_text("HEALTHCHECK CMD curl --fail http://localhost || exit 1")
    
    def add(
        self,
        from_dir: str,
        to_dir: str
    ):
        self.add_text(f"ADD {from_dir} {to_dir}")

    RUN = run
    WORKDIR = workdir
    COPY = copy
    EXPOSE = expose
    CMD = cmd
    entrypoint = cmd
    ENTRYPOINT = cmd
    FROM = set_from
    ARG = arg
    ENV = env
    HEALTHCHECK = helpthcheck
    ADD = add


    @property
    def docker_text(self) -> str:
        """Text of Docker / متن داکر"""
        return self.text_docker



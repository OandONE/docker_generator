from enum import Enum
from typing import Union, Optional

class ImageType(Enum):
    # -----------------------------
    # Runtimes / Languages
    # -----------------------------
    PYTHON = "python"
    NODE = "node"
    GOLANG = "golang"
    OPENJDK = "openjdk"
    ECLIPSE_TEMURIN = "eclipse-temurin"
    PHP = "php"
    RUBY = "ruby"
    DOTNET_SDK = "mcr.microsoft.com/dotnet/sdk"
    DOTNET_RUNTIME = "mcr.microsoft.com/dotnet/aspnet"
    RUST = "rust"

    # -----------------------------
    # Base OS Images
    # -----------------------------
    UBUNTU = "ubuntu"
    DEBIAN = "debian"
    ALPINE = "alpine"
    BUSYBOX = "busybox"
    CENTOS = "centos"
    ROCKY = "rockylinux"
    FEDORA = "fedora"
    SCRATCH = "scratch"  # کاملاً خالی، برای multi-stage

    # -----------------------------
    # Services / Databases / Tools
    # -----------------------------
    NGINX = "nginx"
    MYSQL = "mysql"
    POSTGRES = "postgres"
    REDIS = "redis"
    MONGO = "mongo"
    MARIADB = "mariadb"
    RABBITMQ = "rabbitmq"
    ELASTICSEARCH = "elasticsearch"
    MEMCACHED = "memcached"
    CURL = "curlimages/curl"
    TERRAFORM = "hashicorp/terraform"

    # -----------------------------
    # Special / variants (optional)
    # -----------------------------
    PYTHON_SLIM = "python:slim"
    PYTHON_ALPINE = "python:alpine"
    NODE_ALPINE = "node:alpine"

class From:
    @staticmethod
    def image(
        name: Union[str, ImageType],
        tag: str = "latest",
        variant: Optional[str] = None
    ) -> str:
        """
        Generate a FROM line for Dockerfile.
        name: docker image name (can be anything on Docker Hub)
        tag: tag or version
        variant: optional variant like 'slim' or 'alpine'
        """
        if isinstance(name, ImageType):
            name = name.value
        if variant:
            tag = f"{tag}-{variant}"
        if ":" in name:
            return f"FROM {name}"
        return f"FROM {name}:{tag}"


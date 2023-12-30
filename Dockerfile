ARG RUNTIME_VERSION="3.12"

FROM public.ecr.aws/lambda/python:${RUNTIME_VERSION}

# Install dependencies and fonts
RUN dnf install -y \
        pango \
        zlib-devel \
        libjpeg-turbo-devel \
        openjpeg2-devel \
        libffi-devel \
        ipa-gothic-fonts \
        ipa-mincho-fonts \
        ipa-pgothic-fonts \
        ipa-pmincho-fonts \
    && rm -rf /var/cache/yum/* \
    && dnf clean all

# Change font cache directory
ENV FONTCONFIG_PATH=/var/task
COPY fonts.conf ./
RUN fc-cache --really-force --verbose

# Setup application
COPY app/* ./
RUN pip install -r requirements.txt

CMD [ "index.lambda_handler" ]

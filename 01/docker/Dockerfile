FROM quay.io/centos/centos:stream9
RUN yum install -y openssh-server sudo python3 && \
    yum clean all && \
    ssh-keygen -A && \
    useradd -m -G wheel centos && \
    echo "centos:centos" | chpasswd && \
    echo "%wheel ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
CMD ["/usr/sbin/sshd", "-D"]
EXPOSE 22

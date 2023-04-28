#!/usr/bin/env python3

import subprocess

#definindo uma variuavel para usuario e senha

novo_usu = "luiz"
nova_senha = "abcd"

#cria usuario e senha no sistema linux
subprocess.run(["sudo", "useradd",novo_usu])
subprocess.run(["sudo", "passwd", novo_usu], input=f"{nova_senha}\n{nova_senha}\n".encode())

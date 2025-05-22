# Preparação WSL

## Verificar distribuções disponíveis do Linux

```shell
wsl --list --online
```

## Instalar distribuição Linux Debian

```shell
wsl --install -d Debian
```

## Acessar distribuição Linux Debian

```shell
wsl -d Debian
```

## Habilitar alcance de redes

```shell
sudo rm /etc/resolv.conf
sudo bash -c 'echo "nameserver 8.8.8.8" > /etc/resolv.conf'
sudo bash -c 'echo "[network]" > /etc/wsl.conf'
sudo bash -c 'echo "generateResolvConf = false" >> /etc/wsl.conf'
sudo chattr +i /etc/resolv.conf
```

## Atualizar os pacotes de instalção do Linux Debian

```shell
sudo apt update && sudo apt full-upgrade
```

## Instalar o Python 3

```shell
sudo apt-get install python-is-python3
```

## Verificar a instalação do Python 3

```shell
python --version
```

## Instalar o PIP

```shell
python -m pip install --upgrade pip
```

## Verificar a instalação do PIP

```shell
pip --version
```

## Baixar Java JDK 

```shell
mkdir ~/java/ && cd ~/java/
wget https://download.java.net/java/GA/jdk21.0.2/f2283984656d49d69e91c558476027ac/13/GPL/openjdk-21.0.2_linux-x64_bin.tar.gz
```

## Descompactar Java JDK 

```shell
cd ~/java/
tar -xvf openjdk-21.0.2_linux-x64_bin.tar.gz && rm -Rf openjdk-21.0.2_linux-x64_bin.tar.gz
```

## Incluir variável de ambiente JAVA_HOME

```shell
# JAVA
export JAVA_HOME=~/java/jdk-21.0.2
export PATH=$PATH:$JAVA_HOME/bin
```

## Baixar Spark 3.5.5

```shell
mkdir ~/apache/ && cd ~/apache/
wget https://dlcdn.apache.org/spark/spark-3.5.5/spark-3.5.5-bin-hadoop3.tgz
```

## Descompactar Spark 3.5.5

```shell
cd ~/apache/
tar -xvf spark-3.5.5-bin-hadoop3.tgz && rm spark-3.5.5-bin-hadoop3.tgz
mv spark-3.5.5-bin-hadoop3 spark-3.5.5
```

## Incluir variável de ambiente SPARK_HOME

```shell
# SPARK
export SPARK_HOME=~/apache/spark-3.5.5
export SPARK_LOCAL_IP=127.0.0.1
export HADOOP_HOME=$SPARK_HOME
export PYTHONPATH=$SPARK_HOME/python
export PATH=$PATH:$SPARK_HOME/bin
```

## Recarregar ambiente

```shell
source ~/.bashrc
```

## Verificar instalação Java e Spark

```shell
java --version && pyspark --version
```

# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.network "forwarded_port", guest: 8888, host: 8888, host_ip: "127.0.0.1"

  config.vm.provider "virtualbox" do |vb|
     vb.memory = "8192"
  end
  config.vm.provision "shell", inline: <<-SHELL
     apt update
     apt install -y python3-pip graphviz
     python3 -m pip install --upgrade pip
     python3 -m pip install jupyter pandas matplotlib seaborn graphviz
     grep -qs 'alias notebook=' ~vagrant/.profile || echo 'alias notebook="jupyter notebook --ip=0.0.0.0 --notebook-dir=/vagrant"' >> ~vagrant/.profile
  SHELL
end

Vagrant.configure("2") do |config|
#  config.vm.synced_folder ".", "/vagrant"
  config.vm.define :lava do |lava|
    lava.vm.box = "generic/debian10"
    #lava.ssh.insert_key = false
    #lava.vm.network :private_network, ip: "192.168.121.86"
    lava.vm.hostname = "lavalab.box"
    #lava.vm.network "forwarded_port", guest: 3000, host: 4000
    lava.vm.provider :libvirt do |domain|
      domain.memory = 2048
      domain.cpus = 2
      domain.nested = true
      domain.storage :file, :size => '32G', :type => 'qcow2'
    end
    config.vm.provision "ansible" do |ansible|
      ansible.become = true
      ansible.verbose = "v"
      ansible.playbook = "playbook.yml"
#      ansible.galaxy_role_file = "requirements.yml"
    end
  end
end

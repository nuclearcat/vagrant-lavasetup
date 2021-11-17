Vagrant.configure("2") do |config|
    config.vm.define :lava do |lava|
    lava.vm.box = "generic/debian10"
    lava.vm.hostname = "lavalab.box"
    lava.vm.network "forwarded_port", guest: 80, host: 18080
    lava.trigger.before :destroy do |trigger|
      trigger.warn = "Removing secrets and tokens"
      trigger.run = {inline: "rm _terms/superuser_password _terms/root_token"}
      trigger.exit_codes = [0, 1]
    end
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
    end
  end
end

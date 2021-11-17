Vagrant.configure("2") do |config|
    config.vm.define :lava do |lava|
    lava.vm.box = "generic/debian10"
    #lava.ssh.insert_key = false
    #lava.vm.network :private_network, ip: "192.168.121.86"
    lava.vm.hostname = "lavalab.box"
    #lava.vm.network "forwarded_port", guest: 3000, host: 4000
    lava.trigger.before :destroy do |trigger|
      trigger.warn = "Removing secrets and tokens"
      trigger.run = {inline: "rm _terms/superuser_password _terms/root_token"}
      trigger.exit_codes = [0, 1]
#      trigger.run_remote = {inline: "pg_dump dbname > /vagrant/outfile"}
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

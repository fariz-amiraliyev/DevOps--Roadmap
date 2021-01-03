- name: add several users
  user:
    name: "{{ item }}"
    state: present
    groups: "wheel"
  loop:
     - testuser1
     - testuser2



- name: optimal yum
  yum:
    name: "{{  list_of_packages  }}"
    state: present

- name: non-optimal yum, slower and may cause issues with interdependencies
  yum:
    name: "{{  item  }}"
    state: present
  loop: "{{  list_of_packages  }}"


- name: add several users
  user:
    name: "{{ item.name }}"
    state: present
    groups: "{{ item.groups }}"
  loop:
    - { name: 'testuser1', groups: 'wheel' }
    - { name: 'testuser2', groups: 'root' }


- name: create a tag dictionary of non-empty tags
  set_fact:
    tags_dict: "{{ (tags_dict|default({}))|combine({item.key: item.value}) }}"
  loop: "{{ tags|dict2items }}"
  vars:
    tags:
      Environment: dev
      Application: payment
      Another: "{{ doesnotexist|default() }}"
  when: item.value != ""

- name: give users access to multiple databases
  mysql_user:
    name: "{{ item[0] }}"
    priv: "{{ item[1] }}.*:ALL"
    append_privs: yes
    password: "foo"
  loop: "{{ ['alice', 'bob'] |product(['clientdb', 'employeedb', 'providerdb'])|list }}"

  # show all the hosts in the inventory
- debug:
    msg: "{{ item }}"
  loop: "{{ groups['all'] }}"

# show all the hosts in the current play
- debug:
    msg: "{{ item }}"
  loop: "{{ ansible_play_batch }}"
There is also a specific lookup plugin inventory_hostnames that can be used like this:

# show all the hosts in the inventory
- debug:
    msg: "{{ item }}"
  loop: "{{ query('inventory_hostnames', 'all') }}"

# show all the hosts matching the pattern, ie all but the group www
- debug:
    msg: "{{ item }}"
  loop: "{{ query('inventory_hostnames', 'all:!www') }}"


  

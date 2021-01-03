
# Blocks allow for logical grouping of tasks and in play error handling.
# Most of what you can apply to a single task (with the exception of loops) can
# be applied at the block level, which also makes it much easier to set data or directives common to the tasks.



tasks:
   - name: Install, configure, and start Apache
     block:
       - name: install httpd and memcached
         yum:
           name:
           - httpd
           - memcached
           state: present

       - name: apply the foo config template
         template:
           src: templates/src.j2
           dest: /etc/foo.conf
       - name: start service bar and enable it
         service:
           name: bar
           state: started
           enabled: True
     when: ansible_facts['distribution'] == 'CentOS'
     become: true
     become_user: root
     ignore_errors: yes    # will continue executing the playbook even if some of the tasks fail.


tasks:
 - name: Handle the error
   block:
     - debug:
         msg: 'I execute normally'
     - name: i force a failure
       command: /bin/false
     - debug:
         msg: 'I never execute, due to the above task failing, :-('
   rescue:
     - debug:
         msg: 'I caught an error, can do stuff here to fix it, :-)'


         - name: Always do X
   block:
     - debug:
         msg: 'I execute normally'
     - name: i force a failure
       command: /bin/false
     - debug:
         msg: 'I never execute :-('
   always:
     - debug:
         msg: "This always executes, :-)"





         - name: Attempt and graceful roll back demo
  block:
    - debug:
        msg: 'I execute normally'
    - name: i force a failure
      command: /bin/false
    - debug:
        msg: 'I never execute, due to the above task failing, :-('
  rescue:
    - debug:
        msg: 'I caught an error'
    - name: i force a failure in middle of recovery! >:-)
      command: /bin/false
    - debug:
        msg: 'I also never execute :-('
  always:
    - debug:
        msg: "This always executes"



         tasks:
   - name: Attempt and graceful roll back demo
     block:
       - debug:
           msg: 'I execute normally'
         changed_when: yes
         notify: run me even after an error
       - command: /bin/false
     rescue:
       - name: make sure all handlers run
         meta: flush_handlers
 handlers:
    - name: run me even after an error
      debug:
        msg: 'This handler runs even on error'

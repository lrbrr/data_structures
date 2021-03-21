# script to follow the common workflow
import os
import subprocess

print('1. Create branch')
print('2. Choose where to work')
print('3. Push branch to remote')
print('4. Finish the branch process')

ch = int(input('Enter the choice to proceed: '))


def current_branch_name():
    proc = subprocess.Popen('git branch --show-current',
                            shell=True, stdout=subprocess.PIPE, )
    output = proc.communicate()[0]
    branch_merge_name = str(output)[2:-3]
    return branch_merge_name


if ch == 1:
    branch_name = input('Enter the branch name: ')
    os.system(f'git branch {branch_name}')
    switch = input('Do you want to switch to newly created branch: "y/n" ')
    if switch == 'y' or switch == 'Y':
        os.system(f'git checkout {branch_name}')
    print('You are working at: ', end='')
    os.system('git branch --show-current')

elif ch == 2:
    os.system('git branch')
    where_to_work = str(input('Type the branch from available list above: '))
    os.system(f'git checkout {where_to_work}')

elif ch == 3:
    print('You are working at: ', end='')
    os.system('git branch --show-current')
    push = input('Confirm to push into remote: "y/n"')
    if push == 'y' or push == 'Y':
        os.system('git status')
        os.system('git add -A')
        msg = input('Message for the commit: ')
        os.system(f'git commit -m {msg}')

        branch_name_string = current_branch_name()

        os.system(f'git push -u origin {branch_name_string}')

elif ch == 4:
    print('You are at: ', end='')
    os.system('git branch --show-current')

    branch_merge_name = current_branch_name()

    finish = input('Finish the branch process: "y/n"')
    if finish == 'y' or finish == 'Y':
        os.system('git checkout main')
        os.system('git pull origin main')
        os.system(f'git merge {branch_merge_name}')
        os.system('git push origin main')
    print('Process completed successfully')

else:
    print('Wrong choice')

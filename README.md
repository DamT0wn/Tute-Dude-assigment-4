# Tute-Dude-assigment-4

This repository was used as a hands-on exercise to practice a variety of Git and GitHub commands in a structured, multi-developer-like environment. The commit history reflects a planned development process, showcasing the following:

Repository Setup: The project began with the creation of a new GitHub repository and was cloned to a local machine using SSH, a standard practice for secure and authenticated access. An SSH key was generated and added to the GitHub account to enable this.

Branching Strategy: A feature-branching workflow was used to isolate development.

An initial branch was created for the user (your_username) to add the project's foundational code.

A second branch (your_name_new) was used to simulate a change that would cause a merge conflict, providing an opportunity to practice conflict resolution.

Two separate feature branches (master_1 and master_2) were created to represent parallel development of the frontend and backend, respectively. This is a common approach in team projects to allow simultaneous work without stepping on each other's toes.

Committing and Merging: Commits were made with clear, descriptive messages to maintain a readable and understandable project history. Changes from the feature branches were merged into the main branch to integrate new features.

Advanced Git Commands: More complex scenarios were handled using powerful Git commands:

git reset --soft was used on the main branch to undo specific commits while keeping the changes staged. This allowed for re-committing a desired state and demonstrated how to surgically modify commit history.

git rebase was performed to cleanly integrate the updated main branch changes back into the master_1 branch. The rebase was executed without squashing commits, preserving the individual commit history for each field addition and maintaining a linear, clean project log.


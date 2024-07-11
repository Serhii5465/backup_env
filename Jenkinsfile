@Library(['PrepEnvForBuild', 'DeployWinAgents']) _

node('master') {
    def config = [
        git_repo_url : "git@github.com:Serhii5465/backup_env.git",
        git_branch : "main",
        git_cred_id : "backup_env_repo_cred",
        stash_includes : "**/*.py",
        stash_excludes : "",
        command_deploy  : "robocopy /E . D:\\system\\scripts\\backup_env",
        func_deploy : ""
    ]

    DeployArtifactsPipelineWinAgents(config)
}
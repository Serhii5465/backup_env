@Library(['PrepEnvForBuild', 'DeployWinAgents']) _

node('master') {
    def config = [
        git_repo_url : "backup_env_repo:Serhii5465/backup_env.git",
        git_branch : "main",
        stash_includes : "**/*.py",
        stash_excludes : "",
        command : "robocopy /E . D:\\system\\scripts\\backup_env"
    ]

    DeployArtifactsPipelineWinAgents(config)
}
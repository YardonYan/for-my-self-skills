# Backfill GitHub contributions from March to May 2026

$repoPath = "D:\Study\AI_Yardon\GitCode\tech-blog-generator-main"
$backfillFile = "$repoPath\contributions\backfill.md"

Set-Location $repoPath

# Create backfill file if not exists
if (-not (Test-Path $backfillFile)) {
    "# Backfill Contributions`n`n" | Set-Content $backfillFile -Encoding UTF8
}

# Date range: March 1, 2026 to May 20, 2026 (stop before today to avoid overlap)
$startDate = Get-Date -Year 2026 -Month 3 -Day 1
$endDate = Get-Date -Year 2026 -Month 5 -Day 20

$currentDate = $startDate
$commitCount = 0
$messageTemplates = @(
    "chore: daily contribution",
    "docs: update notes",
    "refactor: clean up structure",
    "feat: add new section",
    "fix: correct typo",
    "style: format document",
    "chore: maintenance update",
    "docs: add reference link"
)

while ($currentDate -le $endDate) {
    # 70% chance to commit on any given day
    if ((Get-Random -Maximum 100) -lt 70) {
        # 1-3 commits per day
        $dailyCommits = Get-Random -Minimum 1 -Maximum 4
        
        for ($i = 0; $i -lt $dailyCommits; $i++) {
            $hour = Get-Random -Minimum 8 -Maximum 23
            $minute = Get-Random -Minimum 0 -Maximum 60
            $second = Get-Random -Minimum 0 -Maximum 60
            
            $commitDate = Get-Date -Year $currentDate.Year -Month $currentDate.Month -Day $currentDate.Day -Hour $hour -Minute $minute -Second $second
            $dateIso = $commitDate.ToString("yyyy-MM-ddTHH:mm:ss")
            $dateStr = $commitDate.ToString("yyyy-MM-dd")
            
            # Add a line to backfill file
            Add-Content -Path $backfillFile -Value "- $dateStr — update"
            
            # Commit with backdated timestamp
            git add contributions/backfill.md
            $msg = $messageTemplates[(Get-Random -Minimum 0 -Maximum $messageTemplates.Length)]
            $env:GIT_AUTHOR_DATE = $dateIso
            $env:GIT_COMMITTER_DATE = $dateIso
            git commit -m "$msg - $dateStr" --no-edit
            Remove-Item Env:\GIT_AUTHOR_DATE -ErrorAction SilentlyContinue
            Remove-Item Env:\GIT_COMMITTER_DATE -ErrorAction SilentlyContinue
            
            $commitCount++
        }
    }
    
    $currentDate = $currentDate.AddDays(1)
}

Write-Host "Created $commitCount backdated commits" -ForegroundColor Green
Write-Host "Pushing to GitHub..." -ForegroundColor Cyan
git push origin master

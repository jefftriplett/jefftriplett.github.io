require 'html-proofer'

task :test do
  sh "bundle exec jekyll build"
  options = {
    :assume_extension => true,
    :checks_to_ignore => [
      "ImageCheck"
    ],
    :file_ignore => [
      /playlist/,
      /styleguide/,
      /tag/,
      /topics/
    ]
  }
  HTMLProofer.check_directory("./_site", options).run
end

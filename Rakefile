require 'html-proofer'

task :test do
  sh "bundle exec jekyll build"
  options = {
    :assume_extension => true,
    :checks_to_ignore => [
      "ImageCheck"
    ],
    :file_ignore => [
      /categories/,
      /playlist/,
      /styleguide/,
      /tags/,
      /topics/
    ]
  }
  HTMLProofer.check_directory("./_site", options).run
end

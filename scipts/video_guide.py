def get_video_guide():
  from IPython.display import HTML
  # Create an HTML iframe element to embed the YouTube video
  html_code = f"""
  <iframe width="800" height="450" src="https://www.youtube.com/embed/EJL3cIGQMz0?si=rveyz9SSYs56jp48" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>"""
  
  # Display the embedded YouTube video
  HTML(html_code)
  

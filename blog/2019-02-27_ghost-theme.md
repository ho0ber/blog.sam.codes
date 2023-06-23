Title: Ghost Default Theme (Casper) Dark-Mode
Date: 2019-02-27 12:00
Category: Code
Cover: images/ghost.png
Summary: So I really like the default theme that comes with Ghost, but I really dislike light backgrounds. I don't want to go through the trouble of maintaining my own fork of the theme, and while there are dark themes out there, many of them are quite ugly and lack the features of Casper.

_This blog post originally appeared on [hoob.dev](https://hoob.dev/op-z-fun/) and has been copied here to merge all of my historical blog posts into a single blog._

So I really like the default theme that comes with Ghost, but I really dislike light backgrounds. I don't want to go through the trouble of maintaining my own fork of the theme, and while there are dark themes out there, many of them are quite ugly and lack the features of Casper.

My solution? Cheat! Using Ghost's code injection features, I'm able to apply some quick and dirty CSS to update the theme to be more to my liking. I had trouble finding any useful examples of this for Casper, so I thought it might be nice to share mine here. I'll update this post as I continue to tweak this site to my liking.

```
    /* Homepage background color */
    body {
        background-color: #000;
    }
    
    /* Article page background color */
    #site-main {
        background-color: #222;    
    }
    
    /* Article title and author name color */
    .post-full-title, .author-card-name a {
        color: #EEE;
    }
    
    /* Article content background/text color */
    .post-content, .post-full-content {
        color: #DDD;
        background-color: #000;  
    }
    
    /* Article links */
    .post-full-content a {
     	color: #8cccf0;   
    }
    
    /* Emphasis */
    .post-full-content em, .post-full-content strong {
        color: #fff;
    }
    
    /* Floating header on articles */
    .floating-header {
        background-color: #000;
        color: #DDD;
    }
    .floating-header-title, .floating-header-share-label {
        color: #DDD;
    }
    
    /* Inline code (backticks) */
    .post-full-content code {
        background-color: #333;
    }
    
    /* Code blocks */
	.post-full-content pre {
     	background-color: #333;   
    }
```

Just drop the above inside some `<style></style>` tags in your header code-injection, and your Ghost site should look like this one! If you want to theme coral talk for comments like I have below, you can [steal that CSS too](https://hoob.io/talk.css).

UPDATE: This appears to have broken over time. I'm looking into trying out this instead: [https://forum.ghost.org/t/casper-the-dark-mode-enabled-version-free/6634](https://forum.ghost.org/t/casper-the-dark-mode-enabled-version-free/6634)
function confirm(text, callback) {
    var brand = document.querySelector('.navbar__brand');
    var question = document.createElement('div');
    question.classList.add('navbar__brand');
    question.setAttribute('data-original-brand', brand.innerHTML);
    question.setAttribute('id', "continue_reading");
    question.innerHTML = text;
    brand.parentNode.insertBefore(question, brand);
    brand.style.display = 'none';
    
    var buttons = document.createElement('div');
    buttons.classList.add('navbar__brand');
    buttons.setAttribute('id', "continue_reading_buttons");
    buttons.innerHTML = '<button class="button button--primary" style="margin-right:5px;">Yes</button><button class="button button--secondary">No</button>';
    brand.parentNode.insertBefore(buttons, brand);
    buttons.querySelector('button').addEventListener('click', function() {
        question.parentNode.removeChild(question);
        brand.style.display = 'flex';
        buttons.parentNode.removeChild(buttons);
        callback(true);
    });
    buttons.querySelector('button:last-child').addEventListener('click', function() {
        question.parentNode.removeChild(question);
        brand.style.display = 'flex';
        buttons.parentNode.removeChild(buttons);
        callback(false);
    });

    var oldHref = window.location.href;
    setInterval(function() {
        if(oldHref !== window.location.href) {
            oldHref = window.location.href;
            if(question.parentNode != null) {
                question.parentNode.removeChild(question);
                brand.style.display = 'flex';
                // remove the buttons
                buttons.parentNode.removeChild(buttons);
                clearInterval(this);
            }
        }
    }, 100);
}

var loadedScroll = false;

function getCurrentPage() {
    let currentPage = document.URL.split("https://nanosyste.ms/")[1].split("#")[0]; // the subdir with the book
    // if currentPage ends with a slash, remove it
    if(currentPage.endsWith("/")) {
        currentPage = currentPage.slice(0, -1);
    }
    return currentPage;
}

function onDocumentReady(og=true) {
    // on load, ask the user whether they want to scroll to the last position
    if(document.URL != 'https://nanosyste.ms/') { // the subdir with the book
        let currentPage = getCurrentPage();
        let lastScroll = localStorage.getItem("nanosystems-scroll-page_"+currentPage);
        if(document.URL.includes("#continue")) {
            document.documentElement.scrollTop = lastScroll;
        }
        else if(lastScroll && lastScroll > 150) {
            confirm("Continue reading?", function(continueReading) {
                if(continueReading) {
					currentPage = getCurrentPage();
					lastScroll = localStorage.getItem("nanosystems-scroll-page_"+currentPage);
                    document.documentElement.scrollTop = lastScroll;
                }
            });
        }
        if(!loadedScroll) {
            // loadedScroll = true;
            window.addEventListener('scroll', function() {
                let currentPage = getCurrentPage();
                if(currentPage == '') return;
                localStorage.setItem("nanosystems-scroll-page_"+currentPage, document.documentElement.scrollTop);
                localStorage.setItem("nanosystems-last-page", currentPage);
            });
        }
    }

    
	// On homepage, ask about returning to the last read chapter
	if(document.URL == 'https://nanosyste.ms/') {
        let lastPage = localStorage.getItem("nanosystems-last-page");
        if(lastPage && lastPage !== 'undefined') {
            confirm("Continue reading?", function(continueReading) {
                if(continueReading) {
                    if(lastPage === undefined) {
                        lastPage = localStorage.getItem("nanosystems-last-page");
                    }
                    if (lastPage != 'undefined') {
                        window.location.href = 'https://nanosyste.ms/'+lastPage + '#continue';
                    }
                }
            });
        }
    }
	// if the location changes without page reloading via react, call onDocumentReady
	if(og) {
		var oldHref = window.location.href;
		setInterval(function() {
			if(oldHref != window.location.href) {
				oldHref = window.location.href;
				
				onDocumentReady(false);
				clearInterval(this);
			}
		}, 100);
	}
}

if (document.readyState === 'loading' || document.readyState === 'interactive') {
    document.addEventListener('load', function() {
        setTimeout(onDocumentReady, 200);
    });
} else {
    setTimeout(onDocumentReady, 200);
}
/*! videojs-popquiz */

(function (videojs) {
  'use strict';

  var vjs_popquiz = function (options) {
    var overlay = document.createElement('div'),
      player = this,
      marker_timeline = [],
      createPopup,
      removePopup,
      checkAnswer;

    if (!options.src && !options.data) {
      // no data provided.
      return;
    } else if (!options.data) {
      // load in data from src
      // unimplemented!
      return;
    }

    // set some defualts
    for (var i = 0; i < options.data.length; i++) {
      options.data[i]['showing'] = false;
      options.data[i]['answered'] = false;
      options.data[i]['display_till'] = options.data[i].time + 0.5;
      marker_timeline.push({
        time: options.data[i].time,
        text: options.data[i].question
      })
    }

    player.markers({
      markerStyle: {
        'background-color': 'lightblue'
      },
      markers: marker_timeline
    });

    overlay.className = 'vjs-popquiz';
    overlay.style.display = 'none';
    overlay.style.width = player.width() + 'px';
    overlay.style.height = player.height() + 'px';
    player.el().insertBefore(overlay, player.el().getElementsByClassName('vjs-poster')[0]);

    player.on('timeupdate', function () {
      var curtime = player.currentTime();
      var curdata = {};

      for (var i = 0; i < options.data.length; i++) {
        curdata = options.data[i];

        if (curtime >= curdata.time && curtime <= curdata.display_till) {
          if (!curdata.showing && !curdata.answered) {
            player.pause();
            createPopup(curdata);
            curdata.showing = true;
          }
        } else {
          if (curdata.showing) {
            removePopup();
            curdata.showing = false;
          }
        }

      }
    });

    createPopup = function(data) {
      var form = document.createElement('form'),
          div = document.createElement('div'),
          input = document.createElement('input'),
          label = document.createElement('label'),
          br = document.createElement('br'),
          popquizSection = document.createElement('section'),
          popquizContainer = document.createElement('article'),
          questionContainer = div.cloneNode();

      popquizSection.className = "popquiz";
      popquizContainer.innerHTML = "<header><h2>Q: " + data.question + "</h2></header>";

      // kind of hackish
      form.style.width = player.width() - 100 + 'px';
      form.style.height = player.height() - 150 + 'px';

      for (var i = 0; i < data.options.length; i++) {
        var checkbox = input.cloneNode(),
            choice = label.cloneNode();

        checkbox.setAttribute("type", "checkbox");
        checkbox.setAttribute("id", 'choice-'+i);
        checkbox.setAttribute("value", i);
        choice.setAttribute("for", 'choice-'+i);
        choice.textContent = data.options[i][0];
        form.appendChild(checkbox);
        form.appendChild(choice);
        form.appendChild(br.cloneNode());
      }

      var buttons = div.cloneNode();
      buttons.className = "submit-buttons";

      var skipButton = input.cloneNode();
      skipButton.setAttribute("type", "button");
      skipButton.setAttribute("value", "Skip");
      skipButton.addEventListener("click", function(){
        player.play()
      });

      var submitButton = input.cloneNode();
      submitButton.setAttribute("type", "submit");
      submitButton.setAttribute("value", "Submit");

      buttons.appendChild(submitButton);
      buttons.appendChild(br.cloneNode());
      buttons.appendChild(skipButton);

      form.appendChild(buttons);
      form.addEventListener("submit", function(e){
        e.preventDefault();
        checkAnswer(data, submitButton, skipButton);
        return false;
      });

      questionContainer.appendChild(form);
      popquizContainer.appendChild(questionContainer);
      popquizSection.appendChild(popquizContainer);
      overlay.appendChild(popquizSection);
      overlay.style.display = "";
    }

    removePopup = function() {
      overlay.style.display = "none";
      overlay.innerHTML = "";
    }

    checkAnswer = function(data, submitButton, nextButton) {
      var pass = true;

      for (var i = 0; i < data.options.length; i++) {
        if (document.getElementById("choice-"+i).checked != data.options[i][1]){
          pass = false;
        }
      }

      if (pass) {
        alert('You got it right! Good job.');
        submitButton.style.display = "none"
        nextButton.setAttribute("value", "Continue");
      } else {
        alert('That was incorrect. Try again!');
      }
    }

  };

  videojs.plugin('popquiz', vjs_popquiz);
}(window.videojs));

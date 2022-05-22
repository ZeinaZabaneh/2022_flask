"use strict";

// How to play pop-up

window.addEventListener("load", function () {
	setTimeout(
		function open(event) {
			document.querySelector(".popup").style.display = "block";
		},
		1000
	)
});

document.querySelector("#info").addEventListener("click", function () {
	document.querySelector(".popup").style.display = "block";
});

document.querySelector("#close").addEventListener("click", function () {
	document.querySelector(".popup").style.display = "none";
});

// Settings pop-up

document.querySelector("#settings").addEventListener("click", function () {
	document.querySelector(".SettingsPopup").style.display = "block";
});

document.querySelector("#Xclose").addEventListener("click", function () {
	document.querySelector(".SettingsPopup").style.display = "none";
});

// Profile pop-up

document.querySelector("#profile").addEventListener("click", function () {
	document.querySelector(".AccountPopUp").style.display = "block";
});

function darkFunc() {
	let current_theme = $("html").attr("data-theme");
	if (current_theme == "dark") {
		$("html").attr("data-theme", "light");
	} else {
		$("html").attr("data-theme", "dark");
	}
}

// Game Functionality

var code_to_guess = [0, 0, 0, 0];
var colours = ["red", "blue", "green", "orange", "pink", "yellow"];
var message = ["Genius!", "Unbelievable!", "Sensational!", "Amazing!", "Great!", "Nice!", "Not Bad!", "Phew, just made it!", "Ooops! Better luck next time!"]

for (let i = 0; i < code_to_guess.length; i++) {
	code_to_guess[i] = Math.floor(Math.random() * colours.length);
}

var correct_guess = false;

var active_row = 0;
var histogram_values = null;

function row_change() {

	active_row += 1;

	if (active_row > 1) {

		var comparison_guess = code_to_guess.slice();
		var user_guess = [];

		const boxes_in_previous_row = document.getElementsByClassName("row-" + (active_row - 1));

		if (active_row > 1 & active_row < 9) {
			document.getElementById("arrow-row-" + (active_row)).style.display = 'block';
			document.getElementById("arrow-row-" + (active_row - 1)).style.display = 'none';
		}

		for (let i = 0; i < code_to_guess.length; i++) {
			var guess = boxes_in_previous_row[i].getAttribute("data-colour_id");
			user_guess.push(guess);
		}

		var out_of_place_count = 0;
		var correct_place_count = 0;

		for (let i = 0; i < comparison_guess.length; i++) {

			var guess = user_guess[i]
			var actual = comparison_guess[i];

			if (parseInt(guess) == actual) {
				correct_place_count += 1;
				user_guess.splice(i, 1);
				comparison_guess.splice(i, 1);
				i -= 1;
			}
		}

		for (let i = 0; i < user_guess.length; i++) {

			var guess = user_guess[i]

			for (let j = 0; j < comparison_guess.length; j++) {

				var possible_match = comparison_guess[j];

				if (parseInt(guess) == possible_match) {
					out_of_place_count += 1;
					user_guess.splice(i, 1);
					comparison_guess.splice(j, 1);
					i -= 1;
					break;
				}
			}

		}
		if (correct_place_count == 4) {
			correct_guess = true;
			pass_values(active_row - 1);
			var number_guesses = active_row - 1;
			active_row = 0;

			let histogram_values = [1, 1, 1, 1, 1, 1, 1, 1, 1];

			// histogram_results();

			fetch('http://127.0.0.1:5000/histogram')
				.then((response) => {
					return response.json();
				})
				.then((values) => {
					histogram_values = values.result
					// Creating the bar chart pop-up
					var xValues = ["1", "2", "3", "4", "5", "6", "7", "8"];
					var yValues = histogram_values;

					var barColors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red", "pink", "grey"];

					new Chart("myChart", {
						type: "horizontalBar",
						data: {
							labels: xValues,
							datasets: [{
								backgroundColor: barColors,
								data: yValues
							}]
						},
						options: {
							legend: {
								display: false
							},
							title: {
								display: true,
								text: "Your Stats"
							},
							scales: {
								xAxes: [{
									ticks: {
										min: 0,
										max: values.max + 1
									}
								}],
								yAxes: [{
									display: true,
									scaleLabel: {
										display: true,
										labelString: 'Number of Tries'
									}
								}]
							}
						}
					});
				});
		}

		// Creating dynamic game completion message
		if (correct_guess) {
			document.getElementById("Message").innerHTML = message[number_guesses - 1];
			document.getElementById("game-stat").innerHTML = "You guessed the Colourdle in " + [number_guesses] + " out of 8 tries!";
			document.getElementById("success").style.display = "block";
		}


		if (active_row == 9) {
			document.getElementById("Message").innerHTML = message[8];
			document.getElementById("success").style.display = "block";
			pass_values(9); // Passing 9 for not guessed within 8 tries
		}

		document.getElementById("MessageClose").addEventListener("click", function () {
			location.reload(document.querySelector(".popup").style.display = "none");
		});
	}

	// Adding the number to the hint circles and assigning a colour
	$('#correct_place_row_' + (active_row - 1)).text(correct_place_count);
	$('#correct_place_row_' + (active_row - 1)).css("background-color", "YellowGreen");

	$('#out_of_place_row_' + (active_row - 1)).text(out_of_place_count);
	$('#out_of_place_row_' + (active_row - 1)).css("background-color", "orange");

	$('.row-' + (active_row - 1)).css('pointer-events', 'none');

	$('#enter_button').css('pointer-events', 'none');
	$('#enter_button').css('opacity', '40%');
	$('#enter_button').css('animation', 'none');
	$('#enter_button').text('Enter Guess');

	// Changing box colour on click and checking if row is full
	$('.row-' + active_row).click(function (event) {

		var box_id = "#" + $(this).attr('id');

		animateCSS(document.getElementById($(this).attr('id')), 'bounceIn');

		$(box_id).attr('data-colour_id', ((parseInt($(box_id).attr('data-colour_id')) + 1) % colours.length))

		$(box_id).css('background-color', colours[parseInt($(box_id).attr('data-colour_id'))]);

		const boxes_in_active_row = document.getElementsByClassName("row-" + active_row);

		var valid_row_input = true;

		for (let box of boxes_in_active_row) {

			var check = box.getAttribute("data-colour_id");
			if (check == '-1') {
				valid_row_input = false;
			}

		}

		if (valid_row_input) {
			$('#enter_button').css('pointer-events', 'auto');
			$('#enter_button').css('opacity', '100%');
			$('#enter_button').text('Check!');
		}


	});


}

// Creating animations for the boxes (Reference: https://animate.style/ and https://www.freecodecamp.org/news/build-a-wordle-clone-in-javascript/)
const animateCSS = (element, animation, prefix = 'animate__') =>

	new Promise((resolve, reject) => {
		const animationName = `${prefix}${animation}`;
		const node = element
		node.style.setProperty("pointer-events", "none");
		node.style.setProperty('--animate-duration', '0.4s');

		node.classList.add(`${prefix}animated`, animationName);

		function handleAnimationEnd(event) {
			event.stopPropagation();
			node.classList.remove(`${prefix}animated`, animationName);
			node.style.setProperty("pointer-events", "auto");
			resolve('Animation ended');
		}

		node.addEventListener('animationend', handleAnimationEnd, {
			once: true
		});
	});

function pass_values(pass_to_python) {
	$.ajax({
		type: 'POST',
		contentType: 'application/json;charset-utf-08',
		dataType: 'json',
		url: 'http://127.0.0.1:5000/pass_val?value=' + pass_to_python,
		success: function (data) {
			var reply = data.reply;
			if (reply == "success") {
				return;
			} else {
				alert("some error ocured in session agent")
			}
		}
	});
}
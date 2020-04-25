function bouton_paroles(paroles,boutton) {
	paroles.style.display = "none";
	boutton.innerHTML = "Afficher les paroles";
	boutton.addEventListener("click", function() {
		if (paroles.style.display == "none") {
			paroles.style.display = "block";
			boutton.innerHTML = "Cacher les paroles";
		} else {
			paroles.style.display = "none";
			boutton.innerHTML = "Afficher les paroles";
		}
	})
}
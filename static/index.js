const input = document.querySelector("input");
const img = document.querySelector("img");
const btn = document.querySelector("button");

if (input === null) throw new Error("No input");
if (img === null) throw new Error("No img");
if (btn === null) throw new Error("No btn");
input.addEventListener("change", () => {
	const files = input.files;
	if (files === null || files.length === 0) {
		btn.hidden = true;
		img.src = "";
		return;
	}
	btn.hidden = false;
	const url = URL.createObjectURL(files[0]);
	img.src = url;
});

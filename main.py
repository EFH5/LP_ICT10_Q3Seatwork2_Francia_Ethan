from js import document

def check(event=None):
    reg = document.querySelector('input[name="reg"]:checked')
    med = document.querySelector('input[name="med"]:checked')
    grade = document.getElementById("grade").value
    section = document.getElementById("section").value

    output_text = document.getElementById("output-text")
    output_img = document.getElementById("output-img")

    if reg is None or med is None:
        output_text.innerText = "Please answer all questions"
        output_img.src = ""

    elif reg.value != "yes" or med.value != "yes":
        output_text.innerText = "INELIGIBLE: Please make sure to register online and/or submit your medical clearance"

    elif section == "sapphire":
        output_text.innerText = f"G{grade} - Sapphire: Blue Bears. Congratulations!"
        output_img.src = "blue.jpg"

    elif section == "ruby":
        output_text.innerText = f"G{grade} - Ruby: Red Bulldogs. Congratulations!"
        output_img.src = "red.jpg"

    elif section == "emerald":
        output_text.innerText = f"G{grade} - Emerald: Green Hornets. Congratulations!"
        output_img.src = "green.jpg"

    elif section == "topaz":
        output_text.innerText = f"G{grade} - Topaz: Yellow Tigers. Congratulations!"
        output_img.src = "yellow.jpg"


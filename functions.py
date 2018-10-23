import en_puzzles.surgery
import en_puzzles.patients
import en_puzzles.pharmacy
import en_puzzles.exam
import en_puzzles.doctors
import en_puzzles.xray
import we_puzzles.surgery
import we_puzzles.patients
import we_puzzles.pharmacy
import we_puzzles.exam
import we_puzzles.doctors
import we_puzzles.xray


we_puzzles = {
    "surgery": we_puzzles.surgery.surgery(),
    "patients": we_puzzles.patients.patients(),
    "pharmacy": we_puzzles.pharmacy.pharmacy(),
    "exam": we_puzzles.exam.exam(),
    "doctors": we_puzzles.doctors.doctors(),
    "xray": we_puzzles.xray.xray()
}

en_puzzles = {
    "surgery": en_puzzles.surgery.surgery(),
    "patients": en_puzzles.patients.patients(),
    "pharmacy": en_puzzles.pharmacy.pharmacy(),
    "exam": en_puzzles.exam.exam(),
    "doctors": en_puzzles.doctors.doctors(),
    "xray": en_puzzles.xray.xray()
}

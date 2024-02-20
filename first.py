from PIL import Image, ImageDraw, ImageFont
import os

def generate_certificate(student_name, template_path, output_dir):
    # Open the certificate template
    template = Image.open(template_path)

    # Create a drawing object
    draw = ImageDraw.Draw(template)

    # Load the default font with a larger size
    font_size = 200
    font = ImageFont.load_default().font_variant(size=font_size)

    # Specify text color
    text_color = (0, 0, 0)  # Black color for text

    # Draw student name
    draw.text((1500, 1250), f"{student_name}", fill=text_color, font=font)


    # Save the certificate
    output_path = os.path.join(output_dir, f"{student_name}_certificate.png")
    template.save(output_path)

    print(f"E-certificate generated for {student_name} as {output_path}")

# List of student names
students = ["Yash Deep", "Jeet Das", "Ashmita Indra", "Sankalpa Giri", "Soumyashree Das", "Sanjana", "Yashovardhan Singh", "Shubham Kumar Sahay", "Vikram Kumar Sahu", "Ayush Ranjan", "Shamik Bhattacharjee", "Harshita Kashyap", "Shreya Mallik", "Devansh Kumar", "V Nishita Raju", "Anubhav Ranjan", "Farhat Tasnim Laskar", "Shruthi Bangaru", "Abhinav Audukoori", "Kankana Bera", "Soumyadeep Sinha", "Arkadeep Bhattacharyya", "Shashwat Sagar", "Shivam Nad", "Manya Pandey", "Soham Patra", "Abhishek Mishra", "Vaibhav Jain", "Kalishayar Mukherjee", "Shubham Kumar", "Ayush Raj", "Dibyasai Jena", "Siddharth Sengupta", "Bismaya Kanta Dash", "Utkarsh Prakash", "Sumit Gupta", "Shailendra Shukla", "Jayash Prem", "Bedaanntica Paul", "Ayushi Gupta", "Abhijeet Kumar", "Anshuman Khaitan", "Prabal Verma", "Bornik Dekaviraj", "Vishnu Gupta", "Akshat Pandey", "Nitesh", "Shreyanshu Ranjan", "Shashwat Kumar", "Priyansu Rout", "Shriya", "Sayak Gain", "Lakshya Nayyar", "Gaurav Kumar Tripathi", "Biswayan Dhar Choudhury", "Junaid Ul Islam", "Shantanu", "Aditya Pandey", "Rajat Shubhra D. Kumawat", "Dhruv Singh Kushwaha", "Rohit Prasad Gupta", "Pracheesh Pandey", "Suvojit Ghosh", "Keshav Gupta", "Shreyam Kumar Tiwari", "Harsh Katiyar", "Aditya Kumar Tiwari", "Aditya", "Ritik Shankar", "Abhirup Chowdhury", "Abhijeet Singh Thakur", "Himanshu Saini", "Sagnik Ghosh", "Arpit Sharma", "Pulkit Goyal", "Debasis Sikdar", "Uma Sankar Sao", "Kaustubh Rastogi", "Yashita", "Yash Raj", "Kumar Ayush", "Paritosh", "Shree Itee Agarwal", "Anish De", "Akshat Bhadani", "Shrey Kumar Jha", "Arpan Mitra", "Aditi Kumar", "Shaurya Pratap Singh", "Rishikesh Kumar", "Rupam Das", "Sarthak Sinha", "Manash Sangam", "Shitij Rakheja", "Diya Basu", "Suprovo Mallick", "Solo Gourav Chakrobarty", "Aman Raj", "Harsh Pratap", "Kundan Kumar", "Ankit Kumar", "Sunny Srivastava", "Archi Srivastava", "Harsh Rastogi","Vidit Rajani Kant Taunk", "Nandish Navamit", "Harsh Tripathi", "Arnav Thakur", "Samimul Haque", "Adarsh Singh", "Ashwin Khowala", "Harsh Vardhan Singh", "Arkadeep Bhattacharyya", "Siddhartha Basu"]

# Course name and date

# Certificate template path
template_path = "certificate.png"  # Replace with the path to your certificate template

# Output directory
output_dir = "output"  # Replace with the directory where you want to save the generated e-certificates

# Generate certificate for each student
for student_name in students:
    generate_certificate(student_name, template_path, output_dir)

print("All e-certificates generated successfully!")

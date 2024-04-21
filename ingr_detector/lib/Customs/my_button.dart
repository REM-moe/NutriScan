import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:ingr_detector/pages/result.dart';
import 'package:http/http.dart' as http;

class UploadButton extends StatefulWidget {
  const UploadButton({super.key});

  @override
  State<UploadButton> createState() => _UploadButtonState();
}

class _UploadButtonState extends State<UploadButton> {
  final ImagePicker _picker = ImagePicker();

  // ignore: unused_field
  XFile? _image;

  void gotoresultpage() {
    Navigator.push(
        context, MaterialPageRoute(builder: (context) => const MyResult()));
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        color: Colors.brown[100],
        borderRadius: BorderRadius.circular(4),
      ),
      child: Column(
        children: [
          ListTile(
            title: const Text("Upload"),
            subtitle: const Text("click to open gallery"),
            leading: Image.asset("lib/images/chai.png"),
            trailing: const Icon(Icons.upload),
            onTap: () => {
              getImageFromGallery(),
            },
          ),
          SizedBox(height: 10, child: Container()),
          ListTile(
            title: const Text("Capture"),
            subtitle: const Text("click to capture image"),
            leading: Image.asset("lib/images/coffee.png"),
            trailing: const Icon(Icons.camera_alt),
            onTap: () => {
              getImageFromCamera(),
            },
          ),
          if (_image != null) // Check if _image is not null
            FutureBuilder<bool>(
                future: uploadImage(
                    _image!), // Just pass _image to uploadImage directly
                builder: (context, snapshot) {
                  if (snapshot.connectionState == ConnectionState.waiting) {
                    return const CircularProgressIndicator(); // Show loading indicator while uploading
                  } else {
                    if (snapshot.hasError) {
                      return const Text(
                          'Error: Failed to upload image. Please try again.'); // Friendly error message
                    } else {
                      if (snapshot.data == true) {
                        // Image uploaded successfully, navigate to a new page
                        Future.delayed(const Duration(seconds: 2), () {
                          Navigator.push(
                            context,
                            MaterialPageRoute(
                                builder: (context) => const MyResult()),
                          );
                        });
                        return const Text('Image uploaded successfully');
                      } else {
                        return const Text(
                            'Failed to upload image. Please check your internet connection and try again.'); // Informative failure message
                      }
                    }
                  }
                }),
        ],
      ),
    );
  }

  Future getImageFromGallery() async {
    final XFile? image = await _picker.pickImage(source: ImageSource.gallery);
    setState(() {
      _image = image;
    });
  }

  Future getImageFromCamera() async {
    final XFile? image = await _picker.pickImage(source: ImageSource.camera);

    setState(() {
      _image = image;
    });
  }

  Future<bool> uploadImage(XFile image) async {
    try {
      var request = http.MultipartRequest(
        'POST',
        Uri.parse('http://172.20.203.123:50001/upload'),
      );
      request.files.add(await http.MultipartFile.fromPath('image', image.path));
      var response = await request.send();

      if (response.statusCode == 200) {
        return true;
      } else {
        print('Failed to upload image: ${response.statusCode}');
        return false;
      }
    } catch (e) {
      print('Error uploading image: $e');
      return false;
    }
  }
}

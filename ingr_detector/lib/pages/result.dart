import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class MyResult extends StatefulWidget {
  const MyResult({Key? key}) : super(key: key);

  @override
  State<MyResult> createState() => _MyResultState();
}

class _MyResultState extends State<MyResult> {
  List<dynamic>?
      result; // Initialize as List<dynamic> or List<Map<String, dynamic>> if you know the structure
  String? error;

  @override
  void initState() {
    super.initState();
    fetchData();
  }

  Future<void> fetchData() async {
    try {
      final response =
          await http.get(Uri.parse('http://192.168.126.241:50001/get_data'));
      if (response.statusCode == 200) {
        final decodedResponse = jsonDecode(response.body);
        final resultBody = decodedResponse['result'];
        setState(() {
          if (resultBody != null) {
            result =
                List.from(resultBody); // Assuming resultBody is a List<dynamic>
          } else {
            result = []; // Set as empty list if resultBody is null
          }
        });
      } else {
        throw Exception('Failed to load data');
      }
    } catch (e) {
      setState(() {
        error = 'Error: $e';
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.brown[200],
      appBar: AppBar(
        backgroundColor: Colors.brown[200],
        title: const Text("Results"),
      ),
      body: Center(
        child: error != null
            ? Text(error!)
            : result != null
                ? result!.isEmpty
                    ? ListTile(
                        title: const Text('Safe'),
                        subtitle: const Text('No harmful ingredients'),
                        leading: Image.asset("lib/images/chai.png"),
                        trailing: const Icon(Icons.all_inclusive),
                        iconColor: Colors.redAccent,
                      )
                    : ListView.builder(
                        itemCount: result!.length,
                        itemBuilder: (context, index) {
                          var currentResult = result![index];
                          if (currentResult is String) {
                            // If currentResult is a string, directly display it
                            return ListTile(
                              title: Text(currentResult),
                              subtitle: const Text('Not specified'),
                              leading: Image.asset("lib/images/chai.png"),
                              trailing: const Icon(Icons.dangerous),
                              iconColor: Colors.redAccent,
                            );
                          } else if (currentResult is Map<String, dynamic>) {
                            // If currentResult is a map, access its properties and display them
                            return ListTile(
                              title: Text(
                                currentResult['name_of_sub'] ??
                                    currentResult['e_code'] ??
                                    'Not specified',
                              ),
                              subtitle: Text(
                                currentResult['harmfulness'] ?? 'Not specified',
                              ),
                              leading: const Icon(Icons.dangerous),
                              trailing: const Icon(Icons.dangerous),
                              iconColor: Colors.redAccent,
                            );
                          } else {
                            // Handle other types of elements if necessary
                            return ListTile(
                              title: const Text('Safe'),
                              subtitle: const Text('No harmful ingredients'),
                              leading: Image.asset("lib/images/chai.png"),
                              trailing: const Icon(Icons.all_inclusive),
                              iconColor: Colors.redAccent,
                            );
                          }
                        },
                      )
                : ListTile(
                    title: const Text('Safe'),
                    subtitle: const Text('No harmful ingredients'),
                    leading: Image.asset("lib/images/chai.png"),
                    trailing: const Icon(Icons.all_inclusive),
                    iconColor: Colors.redAccent,
                  ), // Show "Safe" if result is null
      ),
    );
  }
}

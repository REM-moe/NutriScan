import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class MyResult extends StatefulWidget {
  const MyResult({Key? key}) : super(key: key);

  @override
  State<MyResult> createState() => _MyResultState();
}

class _MyResultState extends State<MyResult> {
  dynamic result;
  String? error;

  @override
  void initState() {
    super.initState();
    fetchData();
  }

  Future<void> fetchData() async {
    try {
      final response =
          await http.get(Uri.parse('http://127.0.0.1:5000/upload'));
      print(response);
      if (response.statusCode == 200) {
        final decodedResponse = jsonDecode(response.body);
        setState(() {
          result = decodedResponse['result'];
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
                ? result == 'Safe'
                    ? ListTile(
                        title: const Text('Safe for consumption'),
                        leading: Image.asset("lib/images/chai.png"),
                        trailing: const Icon(Icons.all_inclusive),
                        iconColor: Colors.green,
                      )
                    : ListView.builder(
                        itemCount: result.length,
                        itemBuilder: (context, index) {
                          var currentSubstance = result[index];
                          return ListTile(
                            title: Text(
                              currentSubstance['name_of_substance'] ??
                                  'Unknown',
                            ),
                            subtitle: Text(
                              currentSubstance['harmfulness'] ?? 'Unknown',
                            ),
                            leading: const Icon(Icons.dangerous),
                            trailing: const Icon(Icons.dangerous),
                            iconColor: Colors.redAccent,
                          );
                        },
                      )
                : ListTile(
                    title: const Text('Safe for consumption'),
                    leading: Image.asset("lib/images/chai.png"),
                    trailing: const Icon(Icons.all_inclusive),
                    iconColor: Colors.green,
                  ), // Show "Safe for consumption" if result is null
      ),
    );
  }
}

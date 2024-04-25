import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class Myresults extends StatefulWidget {
  const Myresults({Key? key}) : super(key: key);

  @override
  State<Myresults> createState() => _MyresultsState();
}

class _MyresultsState extends State<Myresults> {
  String? _result;

  @override
  void initState() {
    super.initState();
    fetchData();
  }

  Future<void> fetchData() async {
    try {
      final response =
          await http.get(Uri.parse('http://192.168.153.83:5000/get'));
      if (response.statusCode == 200) {
        setState(() {
          _result = response.body;
        });
      } else {
        print('Failed to fetch data: ${response.statusCode}');
      }
    } catch (e) {
      print('Error fetching data: $e');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('My Results'),
        backgroundColor: Colors.brown[200], // Change the app bar color
      ),
      body: _result != null
          ? Center(
              child: _result!.contains(
                      'This context does not mention anything about ingredients or things that are consumed')
                  ? Text('No relevant information available')
                  : ListView(
                      padding: const EdgeInsets.all(
                          8), // Increase padding for better spacing
                      children: _result!.split('\n\n').map((result) {
                        final parts = result.split(':');
                        if (parts.length == 2) {
                          final title = parts[0].trim();
                          final subtitle = parts[1].trim();
                          return Card(
                            elevation: 3, // Add elevation to Card
                            margin: const EdgeInsets.symmetric(
                                vertical: 4,
                                horizontal: 8), // Add margin to Card
                            child: ListTile(
                              title: Text(
                                title,
                                style: const TextStyle(
                                    fontWeight: FontWeight.bold,
                                    color:
                                        Colors.black87), // Change title color
                              ),
                              subtitle: Text(
                                subtitle,
                                style: const TextStyle(
                                    fontStyle: FontStyle.italic,
                                    color: Colors
                                        .black54), // Change subtitle color
                              ),
                              leading: Image.asset("lib/images/coffee.png"),
                              trailing: const Icon(Icons.warning),
                              contentPadding: const EdgeInsets.symmetric(
                                  vertical: 8,
                                  horizontal:
                                      16), // Add content padding to ListTile
                            ),
                          );
                        } else {
                          return const Center(
                            child: SizedBox(child: Text("No info Found")),
                          ); // Return an empty SizedBox if parts doesn't have enough elements
                        }
                      }).toList(),
                    ),
            )
          : const Center(
              child: CircularProgressIndicator(),
            ),
    );
  }
}

import * as React from 'react';
import MapView from 'react-native-maps';
import { StyleSheet, Text, View, Dimensions, Image, TouchableOpacity } from 'react-native';
import logo from './assets/takepicture.png'
import logo2 from './assets/camera.png'


export default function App() {
  // const image = { uri: "https://docs.expo.io/static/images/tutorial/splash.png" };
  return (
    <View style={styles.container}>
      <MapView style={styles.map} />
      <TouchableOpacity style={styles.overlay}>
        <Image style={styles.stretch} source={logo} />
      </TouchableOpacity>
      <TouchableOpacity style={styles.overlay2}>
        <Image style={styles.stretch} source={logo2} />
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  map: {
    width: Dimensions.get('window').width,
    height: Dimensions.get('window').height,
  },
  stretch: {
    width: 200,
    height: 200,
  },
  overlay: {
    position: 'absolute',
    bottom: 350,
    backgroundColor: 'rgba(255, 255, 255, 1)',
  },
  overlay2: {
    position: 'absolute',
    bottom: 750,
    backgroundColor: 'rgba(255, 255, 255, 1)',
  },
});

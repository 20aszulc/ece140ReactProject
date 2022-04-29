import * as React from 'react';
import { View, Text } from 'react-native';
import CircularProgress from 'react-native-circular-progress-indicator';


export default function RecordingScreen({ navigation }) {
    return (
        <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
            <Text
                onPress={() => alert('This is the "Recording" screen.')}
                style={{ fontSize: 26, fontWeight: 'bold' }}>Recording Screen</Text>
            <CircularProgress
                value={99}
                radius={120}
                inActiveStrokeOpacity={0.5}
                activeStrokeWidth={15}
                inActiveStrokeWidth={20}
                progressValueStyle={{ fontWeight: '100', color: 'white' }}
                activeStrokeSecondaryColor="orange"
                inActiveStrokeColor="black"
                duration={5000}
                dashedStrokeConfig={{
                    count: 50,
                    width: 4,
                }}
            />
        
        </View>
    );
}
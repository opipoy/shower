#!/bin/fish
npm run build
npx cap sync android
cd android
./gradlew assembleDebug
nc -l -p 9659 < ./app/build/outputs/apk/debug/app-debug.apk
ls -l ./app/build/outputs/apk/debug/app-debug.apk
cd ..

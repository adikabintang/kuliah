package bintang.com.imagedetection;

import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Rect;
import android.net.Uri;
import android.provider.MediaStore;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.FirebaseApp;
import com.google.firebase.analytics.FirebaseAnalytics;
import com.google.firebase.ml.vision.FirebaseVision;
import com.google.firebase.ml.vision.barcode.FirebaseVisionBarcode;
import com.google.firebase.ml.vision.barcode.FirebaseVisionBarcodeDetector;
import com.google.firebase.ml.vision.barcode.FirebaseVisionBarcodeDetectorOptions;
import com.google.firebase.ml.vision.common.FirebaseVisionImage;
import com.google.firebase.ml.vision.common.FirebaseVisionPoint;
import com.google.firebase.ml.vision.face.FirebaseVisionFace;
import com.google.firebase.ml.vision.face.FirebaseVisionFaceDetector;
import com.google.firebase.ml.vision.face.FirebaseVisionFaceDetectorOptions;
import com.google.firebase.ml.vision.face.FirebaseVisionFaceLandmark;

import org.w3c.dom.Text;

import java.io.IOException;
import java.util.List;

import io.reactivex.Observable;
import io.reactivex.Observer;
import io.reactivex.disposables.Disposable;

public class MainActivity extends AppCompatActivity {
    public final static int PICK_PHOTO_CODE = 1046;
    private static final String TAG = "MCC";
    private FirebaseAnalytics mFirebaseAnalytics;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mFirebaseAnalytics = FirebaseAnalytics.getInstance(this);

        Button pickPhotoButton = (Button) findViewById(R.id.btnPickPhoto);

        pickPhotoButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                pickPhotoFromGallery();

            }
        });
    }

    private void pickPhotoFromGallery() {
        Intent intent = new Intent();
        intent.setType("image/*");
        intent.setAction(Intent.ACTION_GET_CONTENT);

        startActivityForResult(intent, PICK_PHOTO_CODE);
    }

    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (data != null) {
            Uri photoUri = data.getData();
            // Do something with the photo based on Uri
            try {
                Bitmap selectedImage = MediaStore.Images.Media.getBitmap(this.getContentResolver(), photoUri);
                // Load the selected image into a preview
                ImageView ivPreview = (ImageView) findViewById(R.id.displayImage);
                ivPreview.setImageBitmap(selectedImage);
                detectImage(selectedImage);

            }
            catch (IOException e) {
                Log.e(TAG, e.getMessage());
            }

        }
    }

    //private List<FirebaseVisionBarcode> detectBarcode(Bitmap originalBitmapImage) {
    private void detectImage(Bitmap originalBitmapImage) {

            FirebaseVisionBarcodeDetectorOptions options =
                new FirebaseVisionBarcodeDetectorOptions.Builder()
                        .setBarcodeFormats(
                                FirebaseVisionBarcode.FORMAT_QR_CODE)
                        .build();

        FirebaseVisionImage image = FirebaseVisionImage.fromBitmap(originalBitmapImage);

        FirebaseVisionBarcodeDetector detector = FirebaseVision.getInstance()
               .getVisionBarcodeDetector(options);


        Task<List<FirebaseVisionBarcode>> result = detector.detectInImage(image)
                .addOnSuccessListener(new OnSuccessListener<List<FirebaseVisionBarcode>>() {
                    @Override
                    public void onSuccess(List<FirebaseVisionBarcode> barcodes) {
                        // Task completed successfully
                        // ...
                        Log.d(TAG, "onSuccess called");
                        if (barcodes.isEmpty()) {
                            Log.d(TAG, "NO QR JIR");
                            // cek gambar muka orang
                            TextView barcodeTxt = (TextView) findViewById(R.id.txtBarcode);
                            barcodeTxt.setText("no");
                            detectFaces(originalBitmapImage);
                        }
                        else {
                            Log.d(TAG, "QR ADA");
                            TextView barcodeTxt = (TextView) findViewById(R.id.txtBarcode);
                            barcodeTxt.setText("yes");
                        }
                    }
                })
                .addOnFailureListener(new OnFailureListener() {
                    @Override
                    public void onFailure(@NonNull Exception e) {
                        // Task failed with an exception
                        // ...
                        Log.e(TAG, "on error called");
                    }
                });

    }

    private void detectFaces(Bitmap originalBitmapImage) {

        FirebaseVisionFaceDetectorOptions options =
                new FirebaseVisionFaceDetectorOptions.Builder()
                        .setModeType(FirebaseVisionFaceDetectorOptions.ACCURATE_MODE)
                        .setLandmarkType(FirebaseVisionFaceDetectorOptions.ALL_LANDMARKS)
                        .setClassificationType(FirebaseVisionFaceDetectorOptions.ALL_CLASSIFICATIONS)
                        .setMinFaceSize(0.15f)
                        .setTrackingEnabled(true)
                        .build();

        FirebaseVisionImage image = FirebaseVisionImage.fromBitmap(originalBitmapImage);
        FirebaseVisionFaceDetector detector = FirebaseVision.getInstance()
                .getVisionFaceDetector(options);

        Task<List<FirebaseVisionFace>> result =
                detector.detectInImage(image)
                        .addOnSuccessListener(
                                new OnSuccessListener<List<FirebaseVisionFace>>() {
                                    @Override
                                    public void onSuccess(List<FirebaseVisionFace> faces) {
                                        // Task completed successfully
                                        // ...
                                        TextView txtNumPeople = (TextView) findViewById(R.id.txtNumPeople);

                                        if (!faces.isEmpty()) {
                                            txtNumPeople.setText(Integer.toString(faces.size()));

                                            for (FirebaseVisionFace face : faces) {
                                                // If classification was enabled:
                                                if (face.getSmilingProbability() != FirebaseVisionFace.UNCOMPUTED_PROBABILITY) {
                                                    float smileProb = face.getSmilingProbability();

                                                    TextView txtSmile = (TextView) findViewById(R.id.txtSmile);
                                                    if (smileProb >= 0.5) {
                                                        txtSmile.setText("yes");
                                                    }
                                                    else {
                                                        txtSmile.setText("no");
                                                    }
                                                }
                                                if (face.getRightEyeOpenProbability() != FirebaseVisionFace.UNCOMPUTED_PROBABILITY) {
                                                    float rightEyeOpenProb = face.getRightEyeOpenProbability();

                                                    TextView txtEyes = (TextView) findViewById(R.id.txtEyes);
                                                    if (rightEyeOpenProb >= 0.5) {
                                                        txtEyes.setText("yes");
                                                    }
                                                    else {
                                                        txtEyes.setText("no");
                                                    }
                                                }

                                            }
                                        }
                                    }
                                })
                        .addOnFailureListener(
                                new OnFailureListener() {
                                    @Override
                                    public void onFailure(@NonNull Exception e) {
                                        // Task failed with an exception
                                        // ...
                                    }
                                });
    }
}

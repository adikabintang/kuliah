package adikabintang.com.screenmode;

import android.content.pm.ActivityInfo;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.CompoundButton;
import android.widget.Switch;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    private static final String TAG = "MCC";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        final Switch switchView = (Switch) findViewById(R.id.scrChange);

        switchView.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {

                TextView portraitText = (TextView) findViewById(R.id.textPortrait);
                TextView landscapeText = (TextView) findViewById(R.id.textLandscape);

                if (switchView.isChecked()) {
                    Log.d(TAG, "true");
                    setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_LANDSCAPE);
                    portraitText.setVisibility(View.GONE);
                    landscapeText.setVisibility(View.VISIBLE);
                }
                else {
                    Log.d(TAG, "false");
                    setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_PORTRAIT);
                    portraitText.setVisibility(View.VISIBLE);
                    landscapeText.setVisibility(View.GONE);
                }

            }
        });
    }
}

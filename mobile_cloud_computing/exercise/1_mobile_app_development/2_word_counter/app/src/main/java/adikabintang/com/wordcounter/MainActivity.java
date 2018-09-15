package adikabintang.com.wordcounter;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    //private static final String TAG = "MCC";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button button = (Button) findViewById(R.id.button);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                displayTheWordCount(view);
            }
        });
    }

    public void displayTheWordCount(View view) {
        EditText editText = (EditText) findViewById(R.id.textInput);
        String message = editText.getText().toString();
        TextView countView = (TextView) findViewById(R.id.txtCount);
        String textAnswer = "Word Count is: ";

        countView.setText(textAnswer.concat(Integer.toString(wordCount(message))));
    }

    private int wordCount(String input) {
        String[] splittedBySpace = input.trim().split("\\s+");
        if (splittedBySpace[0].isEmpty() || splittedBySpace[0] == null) {
            return 0;
        }
        else {
            return splittedBySpace.length;
        }
    }

}

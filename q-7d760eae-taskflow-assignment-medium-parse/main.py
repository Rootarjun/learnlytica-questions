import csv
import io


def parse_tasks_csv(csv_text):
    if not csv_text or not csv_text.strip():
        return []
    reader = csv.DictReader(io.StringIO(csv_text))
    tasks=[]
    for row in reader:
        # TODO: skip rows with a blank id
        # TODO: build a typed dict (int id, stripped title, int/0 points, bool done)
        task_id=(row.get("id") or "").strip()
        if not task_id:
            continue
        title = (row.get("title")or "").strip()
        points_text=(row.get("points") or "").strip()
        done_text= (row.get("done") or "").strip().lower()

        tasks.append({
            "id":int(task_id),
            "title":title,
            "points":int(points_text) if points_text else 0,
            "done":done_text == "true"
        })
    return tasks
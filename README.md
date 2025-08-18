# flact

バックエンドをPythonのFlask、フロントエンドをReactで作成しているWebアプリケーションです。

## ToDo

### backend

- [ ] blueprintでルーティング分割
- [ ] ToDoのCRUD API実装
  * [ ] POST   /todo/
  * [ ] PUT    /todo/:id/ { id: 1, task: 'xxx', done: true }
  * [ ] GET    /todo/:id/
  * [ ] DELETE /todo/:id

### frontend

- [ ] ToDo APIを叩いてCRUDコンポーネント作成
  * [ ] タスクの一覧表示
  * [ ] タスク作成
  * [ ] 編集
  * [ ] doneの切り替え

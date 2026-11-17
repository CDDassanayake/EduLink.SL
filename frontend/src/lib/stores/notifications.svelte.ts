export interface Notification {
	id: string;
	user_id: string;
	type: string;
	title: string;
	body: string;
	is_read: boolean;
	link: string;
	created_at: string;
}

let notifications = $state<Notification[]>([]);
let unreadCount = $state(0);

export function getNotificationsStore() {
	return {
		get notifications() {
			return notifications;
		},
		
		get unreadCount() {
			return unreadCount;
		},

		addNotification(notification: Notification) {
			notifications = [notification, ...notifications];
			if (!notification.is_read) {
				unreadCount++;
			}
		},

		markAsRead(notificationId: string) {
			notifications = notifications.map(n => 
				n.id === notificationId ? { ...n, is_read: true } : n
			);
			unreadCount = Math.max(0, unreadCount - 1);
		},

		markAllAsRead() {
			notifications = notifications.map(n => ({ ...n, is_read: true }));
			unreadCount = 0;
		},

		clearNotifications() {
			notifications = [];
			unreadCount = 0;
		},

		removeNotification(notificationId: string) {
			const notification = notifications.find(n => n.id === notificationId);
			notifications = notifications.filter(n => n.id !== notificationId);
			if (notification && !notification.is_read) {
				unreadCount = Math.max(0, unreadCount - 1);
			}
		}
	};
}
